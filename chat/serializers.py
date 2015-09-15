from swampdragon.serializers.model_serializer import ModelSerializer


class TodoListSerializer(ModelSerializer):
    class Meta:
        model = 'chat.TodoList'
        publish_fields = ('name', 'description')


class TodoItemSerializer(ModelSerializer):
    class Meta:
        model = 'chat.TodoItem'
        publish_fields = ('done', 'text')
        update_fields = ('done', )