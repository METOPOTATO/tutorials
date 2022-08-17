FROM node:12.18.1-alpine AS build

WORKDIR /vue_app

COPY package.json ./

RUN npm install

COPY . .

RUN npm run build 

FROM nginx:1.19.0-alpine  AS prod-stage

# COPY 