from app import app 
from app import db
  
if __name__ == '__main__': 
    db.create_all()
    app.run(host='0.0.0.0', port=8080, debug=True)

