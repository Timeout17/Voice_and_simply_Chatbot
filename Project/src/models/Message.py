from Project.src.Enums.Role import UserEnum
from dataclasses import dataclass, field
import uuid
import datetime


@dataclass
class MessageClass():
    role: UserEnum | None 
    prompt: str
    time: datetime = field(default_factory=datetime.datetime.now)
    id: str = field(default_factory=uuid.uuid4)

