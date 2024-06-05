package com.intakhab.javabackend;

import lombok.Data;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class ModelService {
    private static final String FLASK_SERVER_URL = "http://localhost:5000";

    public double predictHousePrice(double area, int bedrooms) {

        try {
            RestTemplate restTemplate = new RestTemplate();
            String url = FLASK_SERVER_URL + "/predict";
            String requestPayLoad = "{\"area\": " + area + ", \"bedrooms\": " + bedrooms + "}";
            PredictionResponse response = restTemplate.postForObject(url, requestPayLoad, PredictionResponse.class);
            System.out.println(area+" "+bedrooms);
            return response.getPrediction();

        } catch (Exception e) {
            e.printStackTrace();
            return 0.0;
        }
    }

    @Data
    private static class PredictionResponse {
        private double prediction;
    }
}
