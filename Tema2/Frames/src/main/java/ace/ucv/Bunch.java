package ace.ucv;


import java.util.HashMap;
import java.util.Map;

public class Bunch {
    private Map<String, Object> attributes;

    public Bunch() {
        attributes = new HashMap<>();
    }

    public void addAttribute(String name, Object value) {
        attributes.put(name, value);
    }

    public Object getAttribute(String name) {
        return attributes.getOrDefault(name, "undefined");
    }

    public Map<String, Object> getAllAttributes() {
        return attributes;
    }
}