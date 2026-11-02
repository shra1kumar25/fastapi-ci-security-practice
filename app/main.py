from fastapi import FastAPI

app = FastAPI(title="CI Security Practice API")


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "CI Pipeline Practice Started"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


@app.get("/users/{user_id}")
def get_user(user_id: int) -> dict[str, int | str]:
    return {
        "user_id": user_id,
        "name": "Sravan",
        "role": "Backend Developer",
    }
