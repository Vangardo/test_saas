from pydantic import BaseModel, PositiveInt, Field
import app.api.models.standard as standard
from typing import List

warehouse_id_description = "Onlihub unique warehouse id"
warehouse_title_description = "Onlihub warehouse title"
warehouse_user_id_description = "Onlihub warehouse user id"
warehouse_integration_id_description = "Onlihub warehouse integration id"
warehouse_status_id_description = "Onlihub warehouse status id"

status_title_description = "Onluhib status title"

integration_title_description = "Onluhib integration title"


class WarehouseResponse(BaseModel):
    warehouse_id: PositiveInt = Field(..., description=warehouse_id_description)
    warehouse_title: str = Field(..., description=warehouse_title_description)
    user_id: PositiveInt = Field(..., description=warehouse_user_id_description)
    status_title: str = Field(..., description=status_title_description)
    integration_title: str = Field(..., description=integration_title_description)


class Warehouses(BaseModel):
    data: List[WarehouseResponse]


response_example_warehouse = WarehouseResponse(
    warehouse_id=111222,
    warehouse_title="Warehouse title",
    user_id=1,
    status_title = "Status",
    integration_title = "Integration"
)


common_responses_one = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "example": dict(response_example_warehouse)
            }
        }},
    400: standard.bad_request,
    401: standard.auth_error,
    404: {
        "description": "Not Found",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Warehouse was not found"
                }
            }
        }
    }
}
