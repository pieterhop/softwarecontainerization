## The frontend files, built with react. <br />
### To run it locally navigate to the folder from the terminal and run:<br />
1. **npm install**    (this installs all dependencies) <br />
2. **npm start**      (this runs the server and displays the webpage in a browser on localhost:3000) <br />

## OR <br/>

### To build the container run: <br />
sudo docker build -t ui:dev .

### To run the container after bulding run: <br />
 sudo docker run \
    -it \
    --rm \
    -v ${PWD}:/app \
    -v /app/node_modules \
    -p 3001:3000 \
    -e CHOKIDAR_USEPOLLING=true \
    ui:dev
