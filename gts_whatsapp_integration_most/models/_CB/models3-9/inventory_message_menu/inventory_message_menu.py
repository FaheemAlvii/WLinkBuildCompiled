a
    ʎ(ga  �                	   @   st   d dl Z d dlZd dlmZmZmZ e j�ej�ej�	ej�
e�d��� d dlmZ ddgZG dd� dej�ZdS )	�    N)�fields�models�apiz../../)�Config)�stock.action_report_deliveryzDelivery Slip)zstock.action_report_pickingzPicking Operationsc                   @   s@   e Zd ZdZdZejedddd�Ze	�
d�dd	� �Zd
d� ZdS )�InventoryMessageMenuz whatsapp_contacts.messaging_menuz*whatsapp_contacts.messaging_menu.inventoryTr   ZDocument)Zrequired�default�string�selected_documentc                 C   s   | j rt| ��| j �| _d S �N)r
   r   Zget_template_text�message��self� r   �7models/inventory_message_menu/inventory_message_menu.py�onchange_selected_document   s    z/InventoryMessageMenu.onchange_selected_documentc                 C   s   | j S r   )r
   r   r   r   r   �get_document_name   s    z&InventoryMessageMenu.get_document_nameN)�__name__�
__module__�__qualname__Z_inherit�_namer   Z	Selection�	DOCUMENTSr
   r   Zonchanger   r   r   r   r   r   r      s   
r   )�sys�osZodoor   r   r   �path�append�abspath�join�dirname�__file__Z	global_pyr   r   ZTransientModelr   r   r   r   r   �<module>   s   &