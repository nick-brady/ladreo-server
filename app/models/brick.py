from app import db

class Brick(db.Model):
    __tablename__ = 'bricks'

    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float, nullable=False)
    length = db.Column(db.Float, nullable=False)
    width = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    x_coordinate = db.Column(db.Float, nullable=False)
    y_coordinate = db.Column(db.Float, nullable=False)
    z_coordinate = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Brick {self.id}>'