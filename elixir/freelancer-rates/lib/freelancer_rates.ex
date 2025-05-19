defmodule FreelancerRates do
  def daily_rate(hourly_rate) do
    hourly_rate * 8.0
  end

  def apply_discount(before_discount, discount) do
    dis = before_discount * (discount / 100)
    before_discount - dis
  end

  def monthly_rate(hourly_rate, discount) do
    full_mounth_price = 22 * daily_rate(hourly_rate)
    discounted_price = apply_discount(full_mounth_price, discount)
    trunc(Float.ceil(discounted_price))
  end

  def days_in_budget(budget, hourly_rate, discount) do
    discounted_daily_rate = apply_discount(daily_rate(hourly_rate), discount)
    Float.floor(budget / discounted_daily_rate, 1)
  end
end
