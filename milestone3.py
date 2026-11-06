import os
from dotenv import load_dotenv
from supabase import create_client

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

TEST_CUSTOMER = {
    "name": "Python Test Customer",
    "email": "python.test.m3@example.com"
}


def main():
    print("=" * 50)
    print("       MILESTONE 3 - SUPABASE DATABASE DEMO")
    print("=" * 50)

    # Validate configuration
    if not SUPABASE_URL or not SUPABASE_KEY:
        print("ERROR: Supabase credentials are missing.")
        print("Please configure your local .env file.")
        return

    try:
        # Connect to Supabase
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        print("\n[OK] Connected to Supabase!")

        # Check whether the test customer exists
        existing = (
            supabase.table("customers")
            .select("id, name, email")
            .eq("email", TEST_CUSTOMER["email"])
            .execute()
        )

        if existing.data:
            customer = existing.data[0]
            print("[OK] Test customer already exists.")

        else:
            # Insert customer if not found
            result = (
                supabase.table("customers")
                .insert(TEST_CUSTOMER)
                .execute()
            )

            customer = result.data[0]
            print("[OK] Customer inserted successfully!")

        # Retrieve customer information
        check = (
            supabase.table("customers")
            .select("id, name, email")
            .eq("email", TEST_CUSTOMER["email"])
            .execute()
        )

        print("\nCUSTOMER RECORD")
        print("-" * 50)

        if check.data:
            customer = check.data[0]
            print(f"Customer ID : {customer['id']}")
            print(f"Name        : {customer['name']}")
            print(f"Email       : {customer['email']}")
            print("\n[OK] Customer retrieved successfully!")
        else:
            print("[WARNING] No customer record was returned.")

    except Exception as error:
        print("\n[ERROR] Database operation failed.")
        print(f"Details: {error}")

    print("\n" + "=" * 50)
    print("             DEMO COMPLETED")
    print("=" * 50)


if __name__ == "__main__":
    main()
