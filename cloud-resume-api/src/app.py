import os
import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.client("dynamodb")
TABLE_NAME = os.environ["TABLE_NAME"]
COUNTER_PK = "counter"


def lambda_handler(event, context):
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "OPTIONS,POST",
    }

    # CORS preflight
    if event.get("httpMethod") == "OPTIONS":
        return {"statusCode": 200, "headers": headers, "body": ""}

    try:
        body = json.loads(event.get("body") or "{}")
    except json.JSONDecodeError:
        body = {}

    visitor_id = body.get("visitor_id")
    if not visitor_id:
        return {
            "statusCode": 400,
            "headers": headers,
            "body": json.dumps({"message": "visitor_id is required"}),
        }

    visitor_pk = f"visitor#{visitor_id}"

    try:
        # 1) Try to record this visitor as "seen" only if new
        dynamodb.put_item(
            TableName=TABLE_NAME,
            Item={"pk": {"S": visitor_pk}},
            ConditionExpression="attribute_not_exists(pk)",
        )

        # 2) New visitor → increment the main counter
        update_resp = dynamodb.update_item(
            TableName=TABLE_NAME,
            Key={"pk": {"S": COUNTER_PK}},
            UpdateExpression="ADD #total :inc",
            ExpressionAttributeNames={"#total": "total"},
            ExpressionAttributeValues={":inc": {"N": "1"}},
            ReturnValues="UPDATED_NEW",
        )

        total = int(update_resp["Attributes"]["total"]["N"])

    except ClientError as e:
        if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
            # Visitor already counted → just return current total
            get_resp = dynamodb.get_item(
                TableName=TABLE_NAME,
                Key={"pk": {"S": COUNTER_PK}},
            )
            if "Item" in get_resp:
                total = int(get_resp["Item"]["total"]["N"])
            else:
                total = 0
        else:
            print("ERROR:", e)
            return {
                "statusCode": 500,
                "headers": headers,
                "body": json.dumps({"message": "Internal server error"}),
            }

    return {
        "statusCode": 200,
        "headers": headers,
        "body": json.dumps({"views": total}),
    }
