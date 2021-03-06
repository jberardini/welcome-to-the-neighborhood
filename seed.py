from model import Neighborhood, Service, connect_to_db, db
from server import app

def load_services():
    """Loads services from services.txt"""

    print "Services"

    #prevents adding duplicate entries when the file is rerun
    Service.query.delete()

    #read file and insert data
    for row in open('seed_data/services.txt'):
        name, yelp_code, picture = row.rstrip().split("|")

        service = Service(name=name, yelp_code=yelp_code, picture=picture)

        db.session.add(service)

    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()
    load_services()

