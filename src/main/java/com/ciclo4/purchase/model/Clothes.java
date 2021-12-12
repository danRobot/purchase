package com.ciclo4.purchase.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Document(collection = "clothes")
public class Clothes {

    @Id
    private String reference;

    private String category;

    private String size;

    private String description;

    private boolean availability = true;

    private double price;

    private int quantity;

    private String photography;
}
