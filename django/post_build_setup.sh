if [ -f .post_build_setup_done ]; 
  then
    echo "migration and fixutres already installed"
  else
    echo "sleeping 20 seconds"
    sleep 20
    echo "collect static files"
    python manage.py collectstatic --no-input
    echo "prepare and apply django migrations"
    python manage.py makemigrations && python manage.py migrate
    echo "installing fixtures"
    python manage.py loaddata proposal/fixtures/project.json
    python manage.py loaddata proposal/fixtures/settings.json
    python manage.py loaddata proposal/fixtures/template.json
    python manage.py loaddata proposal/fixtures/textblock.json 
    touch .post_build_setup_done
fi