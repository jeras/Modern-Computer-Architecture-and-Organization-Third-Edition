soft65c02_unit -v -i add-with-carry.yaml                   -b add-with-carry
soft65c02_unit -v -i add-with-no-carry.yaml                -b add-with-no-carry
soft65c02_unit -v -i add-with-signed-overflow.yaml         -b add-with-signed-overflow
soft65c02_unit -v -i add-with-unsigned-overflow.yaml       -b add-with-unsigned-overflow

soft65c02_unit -v -i subtract-with-borrow.yaml             -b subtract-with-borrow
soft65c02_unit -v -i subtract-with-no-borrow.yaml          -b subtract-with-no-borrow
soft65c02_unit -v -i subtract-with-signed-underflow.yaml   -b subtract-with-signed-underflow
soft65c02_unit -v -i subtract-with-unsigned-underflow.yaml -b subtract-with-unsigned-underflow

soft65c02_unit -v -i Ex__4_16_bit_addition.yaml            -b Ex__4_16_bit_addition
soft65c02_unit -v -i Ex__5_16_bit_subtraction.yaml         -b Ex__5_16_bit_subtraction
soft65c02_unit -v -i Ex__6_32_bit_addition.yaml            -b Ex__6_32_bit_addition
