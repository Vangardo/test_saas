from . import *
import app.api.models.warehous as wareh_mod
import app.api.processing.warehouses as wareh_proc

router = APIRouter()

@router.get(
    "/warehouses/",
    response_model=wareh_mod.Warehouses,
    responses=wareh_mod.common_responses_one,
    summary="Get warehouses",
    description="This endpoint gets all warehouses",
    tags=['Warehouses'],
    operation_id="get_warehouses"
)
def r_get_warehouses():
    return wareh_proc.get_warehouses()
