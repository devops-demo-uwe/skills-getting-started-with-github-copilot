from fastapi.testclient import TestClient

from src.app import activities, app


client = TestClient(app)


def test_signup_rejects_duplicate_registration():
    activity_name = "Chess Club"
    email = "duplicate-test@mergington.edu"
    participants = activities[activity_name]["participants"]

    try:
        first_response = client.post(
            f"/activities/{activity_name}/signup", params={"email": email}
        )
        duplicate_response = client.post(
            f"/activities/{activity_name}/signup", params={"email": email}
        )

        assert first_response.status_code == 200
        assert duplicate_response.status_code == 400
        assert duplicate_response.json() == {
            "detail": "Student is already signed up for this activity"
        }
        assert participants.count(email) == 1
    finally:
        while email in participants:
            participants.remove(email)