# How To Setup

## This repository uses submodules
- A. Clone this repo along with all its submodules
- B. Clone this repo and the required submodules

## A. First Method
```
git clone --recurse-submodules https://github.com/RickyVu/inserr.git
```

## B. Second Method
### 1. Clone this repo
```
git clone https://github.com/RickyVu/inserr.git
cd inserr
```

### 2. Show the available submodules (alternatively check .gitmodules file)
```
git config --file .gitmodules --get-regexp path
```
- This should give you a result like this:
```
submodule.host/src/inserr_ros.path host/src/inserr_ros
submodule.rov/src/inserr_ros_rov.path rov/src/inserr_ros_rov
```

### 3. Clone the required submodule
```
git submodule init host/src/inserr_ros
git submodule update host/src/inserr_ros
```

---

# Docker Setup
NOTE: Docker development for ROV scripts will be added later
1. Install Docker Desktop
2. Navigate to the desired container configuration folder, i.e the production ready containers for PC/Laptop
```
cd docker-inserr-host
```
2. Docker-Compose using docker-compose.yml files
```
docker-compose up -d --build
```