from Project.src.Enums.Role import UserEnum
from dataclasses import dataclass, field
import uuid
import datetime


@dataclass
class MessageClass():
    id: str = field(default_factory=uuid.uuid4())
    prompt: str
    time: datetime = field(default_factory=datetime.datetime.now())
    role: UserEnum | None 

