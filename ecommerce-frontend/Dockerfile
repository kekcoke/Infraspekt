FROM node:20-alpine AS build
WORKDIR /app
# Set environment to bypass strict ESM resolution and reduce memory usage
ENV GENERATE_SOURCEMAP=false
ENV CI=false
COPY package*.json ./
# Use install with legacy-peer-deps for better compatibility with modern MUI/React combinations
RUN npm install --legacy-peer-deps
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
