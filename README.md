# Server_for_iSpot-iNgress
基本需求:服务层、数据持久化和数据交换、服务端地图操作

## 项目简介

**iSpot-iNgress** 是一个基于 **FastAPI** 和 **PostgreSQL (PostGIS)** 的后端应用，支持通过地理坐标查询附近的用户、活动及兴趣点（POI）。该服务集成了 PostGIS 地理空间数据库功能，支持高效的地理空间查询和处理。

## 环境依赖
- **FastAPI** - 后端框架
- **PostgreSQL** + **PostGIS** - 数据库与地理空间扩展
- **SQLAlchemy** - ORM 数据库操作工具
- **geoalchemy2** - SQLAlchemy 扩展，支持 PostGIS
- **Uvicorn** - ASGI 服务器

## 项目结构
.  
├── app  
│   ├── crud.py **数据库操作(CRUD)**  
│   ├── database.py **数据库连接与初始化**  
│   ├── __init__.py  
│   ├── main.py **FastAPI 入口文件**  
│   ├── models.py **SQLAlchemy 模型定义**   
│   ├── routers  
│   │   ├── events.py **活动相关 API 路由**  
│   │   ├── __init__.py  
│   │   ├── pois.py **兴趣点相关 API 路由**   
│   │   └── users.py **用户相关 API 路由**  
│   └── schemas.py **Pydantic 数据验证模型**  
├── hello.py  
├── LICENSE  
├── README.md **说明文档**  
└── requirements.txt **Python 依赖列表**

## API 说明

1. 查询附近的用户

    GET /users/nearby-users

    该接口允许用户通过传递当前的地理位置（纬度和经度）以及查询的范围（半径），在数据库中的用户表中查找在指定范围内的其他用户，并返回符合条件的用户列表。该接口支持基于地理坐标的查询，范围单位为米。

	请求参数：
	- lat: 纬度（浮点型）
	- lon: 经度（浮点型）
	- radius: 查询半径（以米为单位）

	返回参数：
    - id: 用户的唯一标识符
    - usersname: 用户名
    - location: 用户的地理位置

2. 查询附近的活动

    GET /events/nearby

    该接口允许用户通过传递当前的地理位置（纬度和经度）以及查询的范围（半径），从数据库中的活动表中查找在指定范围内的活动，并返回符合条件的活动列表。每个活动包含活动名称、位置和开始时间。

	请求参数：
	- lat: 纬度（浮点型）
	- lon: 经度（浮点型）
	- radius: 查询半径（以米为单位）

	返回参数：
    - id: 活动的唯一标识符
    - event_name: 活动名
    - location: 活动的地理位置
    - 活动的开始时间

3. 查询附近的兴趣点

    GET /pois/nearby

    该接口允许用户通过传递当前的地理位置（纬度和经度）以及查询的范围（半径），通过调用 高德地图 API 来查找在指定范围内的兴趣点（POI），并返回符合条件的 POI 列表。每个兴趣点包含名称和位置。

	请求参数：
	- lat: 纬度（浮点型）
	- lon: 经度（浮点型）
	- radius: 查询半径（以米为单位）

	返回参数：
    - 参考高德地图返回格式

## 注意事项
该项目需要配置 PostgreSQL 数据库，且必须启用 PostGIS 扩展。高德地图 API 使用需要提供有效的 API Key，并将其配置到代码中。