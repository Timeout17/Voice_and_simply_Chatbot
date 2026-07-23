from Project.src.Enums.Role import UserEnum
from dataclasses import dataclass, field
import uuid
from datetime import datetime


@dataclass
class MessageClass():
    role: UserEnum | None 
    prompt: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    time: datetime = field(default_factory=datetime.now)


