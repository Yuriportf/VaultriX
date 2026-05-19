from app.repositories.transaction_repository import create_transaction


def categorize_transaction(description: str) -> int:
    description = description.lower()

    if "ifood" in description:
        return 1  # Food
    elif "uber" in description:
        return 2  # Transport
    else:
        return 3  # Other


def process_transaction(data: dict, user_id: int):
    description = data.get("description")
    amount = data.get("amount")
    date = data.get("date")

    if not description or not amount or not date:
        raise ValueError("Missing required fields")

    category_id = categorize_transaction(description)

    create_transaction(
        user_id=user_id,
        description=description,
        amount=amount,
        date=date,
        category_id=category_id
    )