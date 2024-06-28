from typing import Annotated
from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', exemple='João', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', exemple='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', exemple=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', exemple=80.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', exemple=1.85)]
    sexo: Annotated[int, Field(description='Sexo do atleta', exemple='M', max_length=1)]