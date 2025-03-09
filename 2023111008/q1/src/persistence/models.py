from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: int
    name: str
    role: str   #* customer or manager
    email: str
    address: str

@dataclass
class DeliveryAgent:
    id: int
    name: str
    available: bool

@dataclass
class Order:
    id: int
    user_id: int
    items: str  #* Comma-separated list of food items
    type: str  #* 'home_delivery' or 'takeaway'
    status: str  #* 'pending', 'preparing', 'out_for_delivery', 'delivered'
    delivery_time: int
    assigned_agent: Optional[int] = None
