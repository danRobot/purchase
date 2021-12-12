package com.ciclo4.purchase.controller;

import java.util.List;
import java.util.Optional;

import com.ciclo4.purchase.model.Orders;
import com.ciclo4.purchase.service.OrdersService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.http.HttpStatus;

@RestController
@RequestMapping("/api/order")
@CrossOrigin
public class OrdersController {
    @Autowired
    private OrdersService servicio;

    /**
     * Servicios GET
     * 
     */
    /** */
    @GetMapping("")
    public String demo(){
        return "<h2>String Test</h2>";
    }
    @GetMapping("/all")
    public List<Orders> demo2(){
        return servicio.listAllOrders();
    }

    @PostMapping("/new")
    @ResponseStatus(HttpStatus.CREATED)
    @CrossOrigin
    public Optional<Orders> save(@RequestBody Orders order){
        return servicio.insertOrder(order);
    }

    @PutMapping("/update")
    @ResponseStatus(HttpStatus.CREATED)
    public Orders update(@RequestBody Orders order){
        return servicio.updateOrder(order);
    }
    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void delete(@PathVariable Integer id) {
        servicio.deleteOrder(id);
    }
    /**
     * 
     */
    @DeleteMapping("/all")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void deleteAll(){
        servicio.deleteAll();
    }
}
