from fastapi import FastAPI, Query, Body, APIRouter

router = APIRouter(prefix="/hotels", tags=["Отели"])

hotels = [
    {"id": 1, "title":"Sochi"},
    {"id": 2, "title":"Dubai"},
]
@router.get("")
def get_hotels(
        id: int | None = Query(None, description="Порядковый номер НП"),
        title: str | None = Query(None, description = "Название населённого пункта"),
):
    hotels_ = []
    for hotel in hotels:
        if id and hotel["id"] != id:
            continue
        if title and hotel["title"] != title:
            continue
        hotels_.append(hotel)
    return hotels_

# body, request body

@router.post("")
def create_hotel(
        title:str = Body(embed=True),
):
    global hotels
    hotels.append({
        "id":hotels[-1]["id"] + 1,
        "title":title,
    })
    return {"status": "ok"}

# Удаляем
@router.delete("/{hotel_id}")
def delete_hotel(hotel_id:int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel["id"] != hotel_id]
    return {"status": "ok"}

@router.put("/{hotel_id}", summary="Изменение данных об отеле",
         description="Если прям вообще жесть то используется description где я сейчас это и пишу")
def edit_hotel(
        hotel_id: int,
        title: str = Body(),
        name: str = Body(),
):
    global hotels
    hotel = [hotel for hotel in hotels if hotel["id"] == hotel_id][0]
    hotel["title"] = title
    hotel["name"] = name
    return {"status":"OKKKK "}

@router.patch("/{hotel_id}", summary="Частичное обновление данных об отеле")
def edit_hotel(
        hotel_id: int,
        title: str | None= Body(None),
        name: str | None= Body(None),
):
    global hotels
    hotel = [hotel for hotel in hotels if hotel["id"] == hotel_id][0]
    if title:
        hotel["title"] = title
    if name:
        hotel["name"] = name
    return {"status":"OKKKK "}

