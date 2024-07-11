from flask import Flask, request, jsonify
from model import db, app, Advertisement
from datetime import datetime

# Создание объявления
@app.route('/advertisements', methods=['POST'])
def create_ad():
    data = request.json
    new_ad = Advertisement(header=data['header'], description=data['description'], created_at=datetime.now(), owner=data['owner'])
    db.session.add(new_ad)
    db.session.commit()
    return jsonify(message='Объявление успешно создана'), 201

# Получение объявления
@app.route('/advertisements/<int:id>', methods=['GET'])
def get_ad(id):
    ad = Advertisement.query.get(id)
    if ad:
        return jsonify(advertisement={'header': ad.header, 'description': ad.description, 'created_at': ad.created_at, 'owner': ad.owner})
    else:
        return jsonify(message='Объявление не найдено'), 404

# Удаление объявления
@app.route('/advertisements/<int:id>', methods=['DELETE'])
def delete_ad(id):
    ad = Advertisement.query.get(id)
    if ad:
        db.session.delete(ad)
        db.session.commit()
        return jsonify(message='Объявление успешно удалена'), 200
    else:
        return jsonify(message='Объявление не найдено'), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
