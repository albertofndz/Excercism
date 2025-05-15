defmodule Lasagna do
  
  def expected_minutes_in_oven() do
    40
  end

  
  def remaining_minutes_in_oven(x) do
    expected_minutes_in_oven() - x
  end

  
  def preparation_time_in_minutes(x) do
    min_per_layer = 2
    min_per_layer * x
  end

  
  def total_time_in_minutes(layers, min_oven) do
    preparation_time_in_minutes(layers) + min_oven
  end

 
  def alarm() do
    "Ding!"
  end
end
