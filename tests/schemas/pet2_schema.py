PET_SCHEMA = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["id", "name", "category", "photoUrls", "tags", "status"],
  "properties": {
    "id": {
      "type": "integer",
      "description": "ID питомца"
    },
    "name": {
      "type": "string",
      "description": "Имя питомца"
    },
    "category": {
      "type": "object",
      "required": ["id"],  # только id обязателен, name - опционально
      "properties": {
        "id": {
          "type": "integer",
          "description": "ID категории"
        },
        "name": {
          "type": "string",
          "description": "Название категории"
        }
      },
      "additionalProperties": False
    },
    "photoUrls": {
      "type": "array",
      "items": {
        "type": "string",
        "format": "uri"
      },
      "description": "Список URL-адресов фотографий"
    },
    "tags": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id"],  # только id обязателен, name - опционально
        "properties": {
          "id": {
            "type": "integer",
            "description": "ID тега"
          },
          "name": {
            "type": "string",
            "description": "Название тега"
          }
        },
        "additionalProperties": False
      }
    },
    "status": {
      "type": "string",
      "enum": ["available", "pending", "sold"],
      "description": "Статус питомца"
    }
  },
  "additionalProperties": False
}