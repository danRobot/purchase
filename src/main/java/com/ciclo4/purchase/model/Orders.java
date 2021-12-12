package com.ciclo4.purchase.model;

import java.util.Date;
import java.util.Map;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Document(collection = "orders")
public class Orders {
    public static String PENDING = "Pendiente";

    public static String APROVED = "Aprobada";

    public static String REJECTED = "Rechazada";

    @Id
    private Integer id;

    private Date registerDay;

    private String status;

    private User salesMan;

    private Map<String, Clothes> products;

    private Map<String, Integer> quantities;

}
