FROM node:22-alpine AS build
WORKDIR /app
# Set environment to bypass strict ESM resolution errors
ENV GENERATE_SOURCEMAP=false
ENV CI=false
COPY package*.json ./
# Install react-transition-group explicitly to ensure resolution
RUN npm install react-transition-group && npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
