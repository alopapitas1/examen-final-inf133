from models.reserva_model import Reserva
from utils.decorator import jwt_required,roles_required
from views.reservas_view import render_reserva_detail,render_reservas_list
import json
from flask import Blueprint,jsonify,request

reserva_bp=Blueprint("reserva",__name__)

@reserva_bp.route("/reservations",methods=["GET"])
@jwt_required
@roles_required(roles=["admin","user"])
def get_reserv():
    reservats=Reserva.get_all()
    return jsonify(render_reservas_list(reservats))

@reserva_bp.route("/reservations",methods=["GET"])
@jwt_required
@roles_required(roles=["admin","user"])
def get_by_id(id):
    resrv=Reserva.get_by_id(id)
    if resrv is None:
        return jsonify({"error":"no se encontro"}),401
    return jsonify(render_reservas_list(resrv))

@reserva_bp.route("/reservations",methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def create_reserva():
    data=request.json
    user_id=data.get("user.id")
    restaurante_id=data.get("restaurante_id")
    reservation_date=data.get("reservation_date")
    num_guests=data.get("num_guests")
    special_requests=data.get("special_requests")
    status=data.get("status")
    
    if user_id is None or restaurante_id is None or reservation_date is None or num_guests is None or special_requests is None or status is None:
        return jsonify({"error":"Faltan datos requeridos"}),400
    
    res=Reserva(user_id=user_id,restaurante_id=restaurante_id,reservation_date=reservation_date,num_guests=num_guests,special_requests=special_requests,status=status)
    res.save()
    return jsonify(render_reserva_detail(res)),201