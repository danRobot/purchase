package com.ciclo4.purchase.service;

import java.util.Date;
import java.util.List;
import java.util.Optional;

import com.ciclo4.purchase.model.Orders;
import com.ciclo4.purchase.reposotory.OrdersRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class OrdersService {
    @Autowired
    private OrdersRepository repositorio;

    /**
     * Devuelve todos los vestidos de la base de datos
     * @return
     */
    public List<Orders> listAllOrders(){
        return repositorio.listAll();
    }

    /**
     * Añade un vestido a la base de Datos
     * @param order
     * @return
     */
    public Optional<Orders> insertOrder(Orders order){
        return repositorio.postOrders(order);
    }

    /**
     * Busca un vestido por el Correo
     * @param reference
     * @return
     */
    public Optional<Orders> getOrderById(Integer reference){
        return repositorio.getClothe(reference);
    }
    public List<Orders> getOrderByZone(String zona){
        return repositorio.getOrdersByZone(zona);
    }
    public List<Orders> getOrdersBySalesman(Integer id){
        return repositorio.getOrdersBySalesman(id);
    }
    public List<Orders> getOrdersByDate(Date date,Integer id){
        return repositorio.getOrdersByDate(date, id);
    }
    public List<Orders> getOrdersByStatus(String status,Integer id){
        return repositorio.getOrdersByStatus(status, id);
    }
    /**
     * Actualiza Usuario
     * @param order
     * @return
     */
    public Orders updateOrder(Orders order){
        return repositorio.putOrders(order);
    }
    public void deleteOrder(Integer id) {
        repositorio.deleteOrder(id);
    }
    /**
     * Borra todos los usuarios de la base de datos
     */
    public void deleteAll(){
        repositorio.deleteAll();;
    }
}
