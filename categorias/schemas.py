from typing import Annotated

from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Nome da Categoria', exemple='Scale', max_length=10)]

class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description='Identificador da categoria')]
