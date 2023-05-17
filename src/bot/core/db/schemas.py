from pydantic import BaseModel, Field

from bot.constants.info.text import FULL_NAME_REGEX
from src.bot.constants.info.text import REGEX_NON_LATIN


class FormBase(BaseModel):
    full_name: str = Field(None, regex=FULL_NAME_REGEX)
    speciality: str = Field(None, regex=REGEX_NON_LATIN)
    job: str = Field(None, regex=REGEX_NON_LATIN)
    experience: str = Field(None, regex=REGEX_NON_LATIN)

    class Config:
        min_anystr_length = 1
        max_anystr_length = 4096
        anystr_strip_whitespace = True
