FROM node:lts-alpine as build-stage

WORKDIR /react_app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]

# RUN npm run build

# FROM nginx:1.17-alpine

# COPY --from=build-stage /react_app/dist /usr/share/nginx/html

# CMD ["nginx", "-g", "daemon off;"]