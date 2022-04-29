const CONFIG = {
  "openapi" : "3.0.0",
  "info" : {
    "description" : "Simple API to send messages to clients.\n",
    "version" : "1.0.0",
    "title" : "Mailing Manager App",
    "license" : {
      "name" : "WTFPL 2",
      "url" : "http://www.wtfpl.net/about/"
    }
  },
  "servers" : [ {
    "description" : "SwaggerHub API Auto Mocking",
    "url" : "https://virtserver.swaggerhub.com/ledorubden/Mailing-manager-app/1.0.0"
  } ],
  "tags" : [ {
    "name" : "recipient",
    "description" : "Everything about your Pets"
  }, {
    "name" : "mailing",
    "description" : "Manage your mailings"
  }, {
    "name" : "message",
    "description" : "Manage your messages"
  }, {
    "name" : "stats",
    "description" : "Check mailing stats",
    "externalDocs" : {
      "description" : "Find out more about our store",
      "url" : "http://swagger.io"
    }
  } ],
  "paths" : {
    "/recipient/" : {
      "get" : {
        "tags" : [ "recipient" ],
        "summary" : "Get all recipients",
        "responses" : {
          "200" : {
            "description" : "Success",
            "content" : {
              "application/json" : {
                "schema" : {
                  "type" : "array",
                  "items" : {
                    "$ref" : "#/components/schemas/recipient"
                  }
                }
              }
            }
          }
        }
      },
      "post" : {
        "tags" : [ "recipient" ],
        "summary" : "Add new recipient",
        "responses" : {
          "201" : {
            "description" : "Success",
            "content" : {
              "application/json" : {
                "schema" : {
                  "$ref" : "#/components/schemas/recipient"
                }
              }
            }
          },
          "400" : {
            "description" : "Invalid input"
          }
        },
        "requestBody" : {
          "$ref" : "#/components/requestBodies/recipient"
        }
      }
    },
    "/recipient/{id}/" : {
      "get" : {
        "tags" : [ "recipient" ],
        "summary" : "Get recipient by id",
        "parameters" : [ {
          "in" : "path",
          "name" : "id",
          "schema" : {
            "type" : "integer"
          },
          "required" : true,
          "description" : "Numeric ID of the recipient to retrieve"
        } ],
        "responses" : {
          "200" : {
            "description" : "Success",
            "content" : {
              "application/json" : {
                "schema" : {
                  "$ref" : "#/components/schemas/recipient"
                }
              }
            }
          },
          "404" : {
            "description" : "Invalid id"
          }
        }
      },
      "put" : {
        "tags" : [ "recipient" ],
        "summary" : "Update an existing recipient",
        "parameters" : [ {
          "in" : "path",
          "name" : "id",
          "schema" : {
            "type" : "integer"
          },
          "required" : true,
          "description" : "Numeric ID of the recipient to update"
        } ],
        "responses" : {
          "200" : {
            "description" : "Success",
            "content" : {
              "application/json" : {
                "schema" : {
                  "$ref" : "#/components/schemas/recipient"
                }
              }
            }
          },
          "400" : {
            "description" : "Invalid input"
          },
          "404" : {
            "description" : "Invalid id"
          }
        },
        "requestBody" : {
          "$ref" : "#/components/requestBodies/recipient"
        }
      },
      "patch" : {
        "tags" : [ "recipient" ],
        "summary" : "Partially update an existing recipient",
        "parameters" : [ {
          "in" : "path",
          "name" : "id",
          "schema" : {
            "type" : "integer"
          },
          "required" : true,
          "description" : "Numeric ID of the recipient to update"
        } ],
        "responses" : {
          "200" : {
            "description" : "Success",
            "content" : {
              "application/json" : {
                "schema" : {
                  "$ref" : "#/components/schemas/recipient"
                }
              }
            }
          },
          "400" : {
            "description" : "Invalid input"
          },
          "404" : {
            "description" : "Invalid id"
          }
        },
        "requestBody" : {
          "$ref" : "#/components/requestBodies/recipient"
        }
      },
      "delete" : {
        "tags" : [ "recipient" ],
        "summary" : "Delete recipient",
        "parameters" : [ {
          "in" : "path",
          "name" : "id",
          "schema" : {
            "type" : "integer"
          },
          "required" : true,
          "description" : "Numeric ID of the recipient to delete"
        } ],
        "responses" : {
          "204" : {
            "description" : "Success"
          },
          "404" : {
            "description" : "Invalid id"
          }
        }
      }
    },
    "/mailing/" : {
      "get" : {
        "tags" : [ "mailing" ],
        "summary" : "Get all mailings",
        "responses" : {
          "200" : {
            "description" : "Success",
            "content" : {
              "application/json" : {
                "schema" : {
                  "type" : "array",
                  "items" : {
                    "$ref" : "#/components/schemas/mailing"
                  }
                }
              }
            }
          }
        }
      },
      "post" : {
        "tags" : [ "mailing" ],
        "summary" : "Add new mailing",
        "responses" : {
          "201" : {
            "description" : "Success",
            "content" : {
              "application/json" : {
                "schema" : {
                  "$ref" : "#/components/schemas/mailing"
                }
              }
            }
          },
          "400" : {
            "description" : "Invalid input"
          }
        },
        "requestBody" : {
          "$ref" : "#/components/requestBodies/mailing"
        }
      }
    },
    "/mailing/{id}/" : {
      "get" : {
        "tags" : [ "mailing" ],
        "summary" : "Get mailing by id",
        "parameters" : [ {
          "in" : "path",
          "name" : "id",
          "schema" : {
            "type" : "integer"
          },
          "required" : true,
          "description" : "Numeric ID of the mailing to retrieve"
        } ],
        "responses" : {
          "200" : {
            "description" : "Success",
            "content" : {
              "application/json" : {
                "schema" : {
                  "$ref" : "#/components/schemas/mailing"
                }
              }
            }
          },
          "404" : {
            "description" : "Invalid id"
          }
        }
      },
      "put" : {
        "tags" : [ "mailing" ],
        "summary" : "Update an existing mailing",
        "parameters" : [ {
          "in" : "path",
          "name" : "id",
          "schema" : {
            "type" : "integer"
          },
          "required" : true,
          "description" : "Numeric ID of the mailing to update"
        } ],
        "responses" : {
          "200" : {
            "description" : "Success",
            "content" : {
              "application/json" : {
                "schema" : {
                  "$ref" : "#/components/schemas/recipient"
                }
              }
            }
          },
          "400" : {
            "description" : "Invalid input"
          },
          "404" : {
            "description" : "Invalid id"
          }
        },
        "requestBody" : {
          "$ref" : "#/components/requestBodies/mailing"
        }
      },
      "patch" : {
        "tags" : [ "mailing" ],
        "summary" : "Partially update an existing mailing",
        "parameters" : [ {
          "in" : "path",
          "name" : "id",
          "schema" : {
            "type" : "integer"
          },
          "required" : true,
          "description" : "Numeric ID of the mailing to update"
        } ],
        "responses" : {
          "200" : {
            "description" : "Success",
            "content" : {
              "application/json" : {
                "schema" : {
                  "$ref" : "#/components/schemas/mailing"
                }
              }
            }
          },
          "400" : {
            "description" : "Invalid input"
          },
          "404" : {
            "description" : "Invalid id"
          }
        },
        "requestBody" : {
          "$ref" : "#/components/requestBodies/mailing"
        }
      },
      "delete" : {
        "tags" : [ "mailing" ],
        "summary" : "Delete mailing",
        "parameters" : [ {
          "in" : "path",
          "name" : "id",
          "schema" : {
            "type" : "integer"
          },
          "required" : true,
          "description" : "Numeric ID of the mailing to delete"
        } ],
        "responses" : {
          "204" : {
            "description" : "Success"
          },
          "404" : {
            "description" : "Invalid id"
          }
        }
      }
    },
    "/message/" : {
      "get" : {
        "tags" : [ "message" ],
        "summary" : "Get all messages",
        "responses" : {
          "200" : {
            "description" : "Success",
            "content" : {
              "application/json" : {
                "schema" : {
                  "type" : "array",
                  "items" : {
                    "$ref" : "#/components/schemas/message"
                  }
                }
              }
            }
          }
        }
      },
      "post" : {
        "tags" : [ "message" ],
        "summary" : "Add new message",
        "responses" : {
          "201" : {
            "description" : "Success",
            "content" : {
              "application/json" : {
                "schema" : {
                  "$ref" : "#/components/schemas/message"
                }
              }
            }
          },
          "400" : {
            "description" : "Invalid input"
          }
        },
        "requestBody" : {
          "$ref" : "#/components/requestBodies/message"
        }
      }
    },
    "/message/{id}/" : {
      "get" : {
        "tags" : [ "message" ],
        "summary" : "Get message by id",
        "parameters" : [ {
          "in" : "path",
          "name" : "id",
          "schema" : {
            "type" : "integer"
          },
          "required" : true,
          "description" : "Numeric ID of the message to retrieve"
        } ],
        "responses" : {
          "200" : {
            "description" : "Success",
            "content" : {
              "application/json" : {
                "schema" : {
                  "$ref" : "#/components/schemas/message"
                }
              }
            }
          },
          "404" : {
            "description" : "Invalid id"
          }
        }
      },
      "put" : {
        "tags" : [ "message" ],
        "summary" : "Update an existing message",
        "parameters" : [ {
          "in" : "path",
          "name" : "id",
          "schema" : {
            "type" : "integer"
          },
          "required" : true,
          "description" : "Numeric ID of the message to update"
        } ],
        "responses" : {
          "200" : {
            "description" : "Success",
            "content" : {
              "application/json" : {
                "schema" : {
                  "$ref" : "#/components/schemas/message"
                }
              }
            }
          },
          "400" : {
            "description" : "Invalid input"
          },
          "404" : {
            "description" : "Invalid id"
          }
        },
        "requestBody" : {
          "$ref" : "#/components/requestBodies/mailing"
        }
      },
      "patch" : {
        "tags" : [ "message" ],
        "summary" : "Partially update an existing message",
        "parameters" : [ {
          "in" : "path",
          "name" : "id",
          "schema" : {
            "type" : "integer"
          },
          "required" : true,
          "description" : "Numeric ID of the message to update"
        } ],
        "responses" : {
          "200" : {
            "description" : "Success",
            "content" : {
              "application/json" : {
                "schema" : {
                  "$ref" : "#/components/schemas/message"
                }
              }
            }
          },
          "400" : {
            "description" : "Invalid input"
          },
          "404" : {
            "description" : "Invalid id"
          }
        },
        "requestBody" : {
          "$ref" : "#/components/requestBodies/message"
        }
      },
      "delete" : {
        "tags" : [ "message" ],
        "summary" : "Delete message",
        "parameters" : [ {
          "in" : "path",
          "name" : "id",
          "schema" : {
            "type" : "integer"
          },
          "required" : true,
          "description" : "Numeric ID of the message to delete"
        } ],
        "responses" : {
          "204" : {
            "description" : "Success"
          },
          "404" : {
            "description" : "Invalid id"
          }
        }
      }
    },
    "/stats/" : {
      "get" : {
        "tags" : [ "stats" ],
        "summary" : "Short stats",
        "responses" : {
          "200" : {
            "description" : "Success",
            "content" : {
              "application/json" : {
                "schema" : {
                  "$ref" : "#/components/schemas/statsSummary"
                }
              }
            }
          }
        }
      }
    },
    "/stats/{id}/" : {
      "get" : {
        "tags" : [ "stats" ],
        "summary" : "Get detailed mailing stats",
        "parameters" : [ {
          "in" : "path",
          "name" : "id",
          "schema" : {
            "type" : "integer"
          },
          "required" : true,
          "description" : "Numeric ID of the message of the mailing"
        } ],
        "responses" : {
          "200" : {
            "description" : "Success",
            "content" : {
              "application/json" : {
                "schema" : {
                  "type" : "array",
                  "items" : {
                    "$ref" : "#/components/schemas/message"
                  }
                }
              }
            }
          }
        }
      }
    }
  },
  "components" : {
    "schemas" : {
      "recipient" : {
        "type" : "object",
        "required" : [ "country_code", "phone_number", "timezone" ],
        "properties" : {
          "id" : {
            "type" : "integer",
            "format" : "int64"
          },
          "country_code" : {
            "type" : "string",
            "maxLength" : 3,
            "example" : 74
          },
          "phone_number" : {
            "type" : "string",
            "example" : 7895411214,
            "maxLength" : 10
          },
          "timezone" : {
            "type" : "string",
            "example" : "America/Asuncion",
            "maxLength" : 50
          },
          "tags" : {
            "type" : "string",
            "example" : "premium_subscriber",
            "description" : "Arbitrary string"
          }
        }
      },
      "mailing" : {
        "type" : "object",
        "required" : [ "start_time", "stop_time", "msg" ],
        "properties" : {
          "id" : {
            "type" : "integer",
            "format" : "int64"
          },
          "start_time" : {
            "type" : "string",
            "format" : "date-time",
            "example" : "2022-04-29T03:15:00+03:00"
          },
          "stop_time" : {
            "type" : "string",
            "format" : "date-time",
            "example" : "2022-04-29T03:20:00+03:00"
          },
          "msg" : {
            "type" : "string",
            "example" : "Hello, world!"
          },
          "filters" : {
            "type" : "object"
          }
        }
      },
      "message" : {
        "type" : "object",
        "required" : [ "mailing", "recipient" ],
        "properties" : {
          "id" : {
            "type" : "integer",
            "format" : "int64"
          },
          "mailing" : {
            "type" : "integer",
            "format" : "int64"
          },
          "recipient" : {
            "type" : "integer",
            "format" : "int64"
          },
          "date_sent" : {
            "type" : "string",
            "format" : "date-time",
            "example" : "2022-04-29T03:15:00+03:00"
          },
          "status" : {
            "type" : "string",
            "enum" : [ "pending", "success", "fail" ],
            "default" : "pending"
          }
        }
      },
      "statsSummary" : {
        "type" : "array",
        "items" : {
          "type" : "object",
          "properties" : {
            "id" : {
              "type" : "integer",
              "format" : "int64"
            },
            "pending" : {
              "type" : "integer",
              "format" : "int32"
            },
            "fail" : {
              "type" : "integer",
              "format" : "int32"
            },
            "success" : {
              "type" : "integer",
              "format" : "int32"
            }
          }
        }
      }
    },
    "requestBodies" : {
      "recipient" : {
        "content" : {
          "application/json" : {
            "schema" : {
              "$ref" : "#/components/schemas/recipient"
            }
          }
        },
        "required" : true
      },
      "mailing" : {
        "content" : {
          "application/json" : {
            "schema" : {
              "$ref" : "#/components/schemas/mailing"
            }
          }
        },
        "required" : true
      },
      "message" : {
        "content" : {
          "application/json" : {
            "schema" : {
              "$ref" : "#/components/schemas/message"
            }
          }
        },
        "required" : true
      }
    }
  }
}