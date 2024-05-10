import sqlalchemy
from flask import Flask, jsonify
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from models import Freelancer, Base, engine, session, Customer

app = Flask(__name__)

admin = Admin(app, name='Панель управления', template_mode='bootstrap3')

admin.add_view(ModelView(Freelancer, session))
admin.add_view(ModelView(Customer, session))


def before_request_func():
    try:
        Base.metadata.create_all(engine)
        objects = [Freelancer(id=1, name="Victor Ivanov", experience="Middle+ Python developer",
                              contacts="best_dev@mail.us"),
                   Customer(id=1, name="Alex Alexeev", experience="HR in GYS-company",
                            contacts="best_hr@mail.us")]

        session.bulk_save_objects(objects)
        session.commit()
    except sqlalchemy.exc.IntegrityError:
        pass


@app.route("/", methods=["GET"])
def get_base():
    before_request_func()
    return "Hello"


@app.route("/for_freelancers/<int:id>", methods=["GET"])
def get_freelancer(id):
    freelancer = session.query(Freelancer).filter_by(id=id).first()
    if freelancer:
        freelancer_info = {
            'name': freelancer.name,
            'experience': freelancer.experience,
            'contacts': freelancer.contacts
        }
        return jsonify(freelancer_info)
    else:
        return jsonify({'error': 'Not found'}), 404


@app.route("/for_customers/<int:id>", methods=["GET"])
def get_customer(id):
    customer = session.query(Customer).filter_by(id=id).first()
    if customer:
        customer_info = {
            'name': customer.name,
            'experience': customer.experience,
            'contacts': customer.contacts
        }
        return jsonify(customer_info)
    else:
        return jsonify({'error': 'Not found'}), 404


if __name__ == '__main__':
    app.run()
