#!/usr/bin/env python

# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from locust import HttpUser, TaskSet, task


class MetricsTaskSet(TaskSet):
    def on_start(self):
        self.client.headers = dict(
            {"Authorization": "XXXX", "Content-Type": "application/json"})

    @task(1)
    def get_carts(self):
        self.client.get(
            '/cart-service/stores/12345/cart',
            headers=self.client.headers
        )

    @task(1)
    def post_cart(self):
        self.client.post(
            "/cart-service/stores/12345/cart",
            json={
                "ipAddress": "127.0.0.1",
                "shopperId": "hello",
                "phone": "512-123-4567",
                "cartItems": [
                    {
                        "productId": "abc",
                        "quantity": 1,
                        "giftWrapNote": "best wishes for you and yours",
                        "price": "10.00"
                    },
                    {
                        "productId": "def",
                        "quantity": 2
                    }
                ],
                "cartDiscounts": [
                    {
                        "discountCode": "all"
                    },
                    {
                        "discountCode": "your"
                    },
                    {
                        "discountCode": "base"
                    }
                ]
            },
            headers=self.client.headers
        )


class MetricsLocust(HttpUser):
    tasks = [MetricsTaskSet]
