from fastapi import APIRouter, Body, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from .models import (
    Ingredient,
    Gusto,
    Imagen,
    Comentario,
    Publicacion,
    UpdatePublicacionModel,
)

router = APIRouter()


@router.post("/", response_description="Add new blog")
async def create_task(request: Request, publicacion: Publicacion = Body(...)):
    pub = jsonable_encoder(publicacion)
    new_pub = await request.app.mongodb["publicaciones"].insert_one(pub)
    created_pub = await request.app.mongodb["publicaciones"].find_one(
        {"_id": new_pub.inserted_id}
    )

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_pub)


@router.get("/", response_description="List all blogs")
async def list_tasks(request: Request):
    publicaciones = []
    for pub in await request.app.mongodb["publicaciones"].find().to_list(length=100):
        publicaciones.append(pub)
    return publicaciones


@router.get("/{id}", response_description="Get a single blog")
async def show_blog(id: str, request: Request):
    if (
        pub := await request.app.mongodb["publicaciones"].find_one({"_id": id})
    ) is not None:
        return pub

    raise HTTPException(status_code=404, detail=f"Blog {id} not found")


@router.put("/{id}", response_description="Update a blog")
async def update_blog(
    id: str, request: Request, pub: UpdatePublicacionModel = Body(...)
):
    pub = {k: v for k, v in pub.dict().items() if v is not None}

    if len(pub) >= 1:
        update_result = await request.app.mongodb["publicaciones"].update_one(
            {"_id": id}, {"$set": pub}
        )

        if update_result.modified_count == 1:
            if (
                updated_blog := await request.app.mongodb["publicaciones"].find_one(
                    {"_id": id}
                )
            ) is not None:
                return updated_blog

    if (
        existing_blog := await request.app.mongodb["publicaciones"].find_one(
            {"_id": id}
        )
    ) is not None:
        return existing_blog

    raise HTTPException(status_code=404, detail=f"blog {id} not found")


@router.delete("/{id}", response_description="Delete blog")
async def delete_blog(id: str, request: Request):
    delete_result = await request.app.mongodb["publicaciones"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Blog {id} not found")
