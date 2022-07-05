from fastapi import FastAPI
from routes.user_routes import user

app = FastAPI(
    title="Documentation",
    description="API restful, lorem ipsum dolor sit amet.",
    version="1.0",
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    docExpansion="None",terms_of_service="http://example.com/terms/",swagger_ui_parameters={"defaultModelsExpandDepth": -1})

app.include_router(user)