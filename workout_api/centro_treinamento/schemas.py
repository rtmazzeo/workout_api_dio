from typing import Annotated
from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', exemple='Ct King', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do Centro de Treinamento', exemple='Rua das Almas, 30', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do Centro de Treinamento', exemple='João Fortão', max_length=30)]

class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', examples=['CT King'], max_length=20)]


class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]  
