# TODO(M6): switch to a multi-stage production build (deps -> build -> standalone runner)
FROM node:22-alpine
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
CMD ["npm", "run", "dev"]
