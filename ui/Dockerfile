# pull official base image
FROM node:13.12.0-alpine AS builder

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent
#RUN npm install react-scripts@3.4.1 -g --silent

# add app
COPY . ./

#build
RUN npm run build

#STAGE-2

#nginx base img
FROM nginx:1.19.0

#copies React to the container directory
# Set working directory to nginx resources directory
WORKDIR /usr/share/nginx/html
# Remove default nginx static resources
RUN rm -rf ./*
# Copies static resources from builder stage
COPY --from=builder /app/build .
# Containers run nginx with global directives and daemon off
ENTRYPOINT ["nginx", "-g", "daemon off;"]
# start app
#CMD ["npm", "start"]
