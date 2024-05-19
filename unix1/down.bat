for container_id in $(docker ps -a -q); do
    docker stop $container_id
done


