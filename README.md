<h1 align="center">ExRates</h1>
    <blockquote>Простая библиотека, которая выдает данные о курсе более простым способом</blockquote>
</p>
<hr>

## Установка
1) С помощью установщика pip из GitHub: 
   
   ```sh
   pip3 install https://github.com/Infqq/exrates/archive/main.zip --upgrade
   ```

### Example

```python
from exrates import *

check = currency()
result = check.get('USD')
print(result)
```
