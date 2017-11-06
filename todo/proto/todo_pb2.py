# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='todo.proto',
  package='todo',
  syntax='proto3',
  serialized_pb=_b('\n\ntodo.proto\x12\x04todo\"\x9d\x01\n\x04Todo\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x11\n\tcreatedOn\x18\x04 \x01(\x01\x12\r\n\x05\x64ueOn\x18\x05 \x01(\x01\x12\x13\n\x0b\x63ompletedOn\x18\x06 \x01(\x01\x12\x1c\n\x06status\x18\x07 \x01(\x0e\x32\x0c.todo.Status\x12\x10\n\x08\x61ssignee\x18\x08 \x01(\x03\"*\n\x0e\x41\x64\x64TodoRequest\x12\x18\n\x04todo\x18\x01 \x01(\x0b\x32\n.todo.Todo\".\n\x0eGetTodoRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08\x61ssignee\x18\x02 \x01(\x03\"3\n\x13\x43ompleteTodoRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08\x61ssignee\x18\x02 \x01(\x03\"D\n\x12GetByStatusRequest\x12\x1c\n\x06status\x18\x01 \x01(\x0e\x32\x0c.todo.Status\x12\x10\n\x08\x61ssignee\x18\x02 \x01(\x03\"Q\n\x13UpdateStatusRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x1c\n\x06status\x18\x02 \x01(\x0e\x32\x0c.todo.Status\x12\x10\n\x08\x61ssignee\x18\x03 \x01(\x03\"+\n\x0f\x45\x64itTodoRequest\x12\x18\n\x04todo\x18\x01 \x01(\x0b\x32\n.todo.Todo\"H\n\x0cTodoResponse\x12\x18\n\x04todo\x18\x01 \x01(\x0b\x32\n.todo.Todo\x12\x1e\n\x05\x65rror\x18\x02 \x01(\x0e\x32\x0f.todo.ErrorCode\"S\n\x16TodoCollectionResponse\x12\x19\n\x05todos\x18\x01 \x03(\x0b\x32\n.todo.Todo\x12\x1e\n\x05\x65rror\x18\x02 \x01(\x0e\x32\x0f.todo.ErrorCode*-\n\x06Status\x12\x08\n\x04TODO\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\x08\n\x04\x44ONE\x10\x02*=\n\tErrorCode\x12\r\n\tNOT_FOUND\x10\x00\x12\x10\n\x0cSERVER_ERROR\x10\x01\x12\x0f\n\x0b\x42\x41\x44_REQUEST\x10\x02\x32\xf2\x02\n\x05Todos\x12\x33\n\x07\x61\x64\x64Todo\x12\x14.todo.AddTodoRequest\x1a\x12.todo.TodoResponse\x12\x33\n\x07getTodo\x12\x14.todo.GetTodoRequest\x1a\x12.todo.TodoResponse\x12=\n\x0c\x63ompleteTodo\x12\x19.todo.CompleteTodoRequest\x1a\x12.todo.TodoResponse\x12J\n\x10getTodosByStatus\x12\x18.todo.GetByStatusRequest\x1a\x1c.todo.TodoCollectionResponse\x12=\n\x0cupdateStatus\x12\x19.todo.UpdateStatusRequest\x1a\x12.todo.TodoResponse\x12\x35\n\x08\x65\x64itTodo\x12\x15.todo.EditTodoRequest\x1a\x12.todo.TodoResponseb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='todo.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TODO', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IN_PROGRESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DONE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=682,
  serialized_end=727,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
_ERRORCODE = _descriptor.EnumDescriptor(
  name='ErrorCode',
  full_name='todo.ErrorCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVER_ERROR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_REQUEST', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=729,
  serialized_end=790,
)
_sym_db.RegisterEnumDescriptor(_ERRORCODE)

ErrorCode = enum_type_wrapper.EnumTypeWrapper(_ERRORCODE)
TODO = 0
IN_PROGRESS = 1
DONE = 2
NOT_FOUND = 0
SERVER_ERROR = 1
BAD_REQUEST = 2



_TODO = _descriptor.Descriptor(
  name='Todo',
  full_name='todo.Todo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='todo.Todo.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='todo.Todo.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='todo.Todo.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='createdOn', full_name='todo.Todo.createdOn', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dueOn', full_name='todo.Todo.dueOn', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='completedOn', full_name='todo.Todo.completedOn', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='todo.Todo.status', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='assignee', full_name='todo.Todo.assignee', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=178,
)


_ADDTODOREQUEST = _descriptor.Descriptor(
  name='AddTodoRequest',
  full_name='todo.AddTodoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='todo', full_name='todo.AddTodoRequest.todo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=222,
)


_GETTODOREQUEST = _descriptor.Descriptor(
  name='GetTodoRequest',
  full_name='todo.GetTodoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='todo.GetTodoRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='assignee', full_name='todo.GetTodoRequest.assignee', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=270,
)


_COMPLETETODOREQUEST = _descriptor.Descriptor(
  name='CompleteTodoRequest',
  full_name='todo.CompleteTodoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='todo.CompleteTodoRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='assignee', full_name='todo.CompleteTodoRequest.assignee', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=272,
  serialized_end=323,
)


_GETBYSTATUSREQUEST = _descriptor.Descriptor(
  name='GetByStatusRequest',
  full_name='todo.GetByStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='todo.GetByStatusRequest.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='assignee', full_name='todo.GetByStatusRequest.assignee', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=325,
  serialized_end=393,
)


_UPDATESTATUSREQUEST = _descriptor.Descriptor(
  name='UpdateStatusRequest',
  full_name='todo.UpdateStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='todo.UpdateStatusRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='todo.UpdateStatusRequest.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='assignee', full_name='todo.UpdateStatusRequest.assignee', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=395,
  serialized_end=476,
)


_EDITTODOREQUEST = _descriptor.Descriptor(
  name='EditTodoRequest',
  full_name='todo.EditTodoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='todo', full_name='todo.EditTodoRequest.todo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=478,
  serialized_end=521,
)


_TODORESPONSE = _descriptor.Descriptor(
  name='TodoResponse',
  full_name='todo.TodoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='todo', full_name='todo.TodoResponse.todo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='todo.TodoResponse.error', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=523,
  serialized_end=595,
)


_TODOCOLLECTIONRESPONSE = _descriptor.Descriptor(
  name='TodoCollectionResponse',
  full_name='todo.TodoCollectionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='todos', full_name='todo.TodoCollectionResponse.todos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='todo.TodoCollectionResponse.error', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=597,
  serialized_end=680,
)

_TODO.fields_by_name['status'].enum_type = _STATUS
_ADDTODOREQUEST.fields_by_name['todo'].message_type = _TODO
_GETBYSTATUSREQUEST.fields_by_name['status'].enum_type = _STATUS
_UPDATESTATUSREQUEST.fields_by_name['status'].enum_type = _STATUS
_EDITTODOREQUEST.fields_by_name['todo'].message_type = _TODO
_TODORESPONSE.fields_by_name['todo'].message_type = _TODO
_TODORESPONSE.fields_by_name['error'].enum_type = _ERRORCODE
_TODOCOLLECTIONRESPONSE.fields_by_name['todos'].message_type = _TODO
_TODOCOLLECTIONRESPONSE.fields_by_name['error'].enum_type = _ERRORCODE
DESCRIPTOR.message_types_by_name['Todo'] = _TODO
DESCRIPTOR.message_types_by_name['AddTodoRequest'] = _ADDTODOREQUEST
DESCRIPTOR.message_types_by_name['GetTodoRequest'] = _GETTODOREQUEST
DESCRIPTOR.message_types_by_name['CompleteTodoRequest'] = _COMPLETETODOREQUEST
DESCRIPTOR.message_types_by_name['GetByStatusRequest'] = _GETBYSTATUSREQUEST
DESCRIPTOR.message_types_by_name['UpdateStatusRequest'] = _UPDATESTATUSREQUEST
DESCRIPTOR.message_types_by_name['EditTodoRequest'] = _EDITTODOREQUEST
DESCRIPTOR.message_types_by_name['TodoResponse'] = _TODORESPONSE
DESCRIPTOR.message_types_by_name['TodoCollectionResponse'] = _TODOCOLLECTIONRESPONSE
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
DESCRIPTOR.enum_types_by_name['ErrorCode'] = _ERRORCODE

Todo = _reflection.GeneratedProtocolMessageType('Todo', (_message.Message,), dict(
  DESCRIPTOR = _TODO,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.Todo)
  ))
_sym_db.RegisterMessage(Todo)

AddTodoRequest = _reflection.GeneratedProtocolMessageType('AddTodoRequest', (_message.Message,), dict(
  DESCRIPTOR = _ADDTODOREQUEST,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.AddTodoRequest)
  ))
_sym_db.RegisterMessage(AddTodoRequest)

GetTodoRequest = _reflection.GeneratedProtocolMessageType('GetTodoRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETTODOREQUEST,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.GetTodoRequest)
  ))
_sym_db.RegisterMessage(GetTodoRequest)

CompleteTodoRequest = _reflection.GeneratedProtocolMessageType('CompleteTodoRequest', (_message.Message,), dict(
  DESCRIPTOR = _COMPLETETODOREQUEST,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.CompleteTodoRequest)
  ))
_sym_db.RegisterMessage(CompleteTodoRequest)

GetByStatusRequest = _reflection.GeneratedProtocolMessageType('GetByStatusRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETBYSTATUSREQUEST,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.GetByStatusRequest)
  ))
_sym_db.RegisterMessage(GetByStatusRequest)

UpdateStatusRequest = _reflection.GeneratedProtocolMessageType('UpdateStatusRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATESTATUSREQUEST,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.UpdateStatusRequest)
  ))
_sym_db.RegisterMessage(UpdateStatusRequest)

EditTodoRequest = _reflection.GeneratedProtocolMessageType('EditTodoRequest', (_message.Message,), dict(
  DESCRIPTOR = _EDITTODOREQUEST,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.EditTodoRequest)
  ))
_sym_db.RegisterMessage(EditTodoRequest)

TodoResponse = _reflection.GeneratedProtocolMessageType('TodoResponse', (_message.Message,), dict(
  DESCRIPTOR = _TODORESPONSE,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.TodoResponse)
  ))
_sym_db.RegisterMessage(TodoResponse)

TodoCollectionResponse = _reflection.GeneratedProtocolMessageType('TodoCollectionResponse', (_message.Message,), dict(
  DESCRIPTOR = _TODOCOLLECTIONRESPONSE,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.TodoCollectionResponse)
  ))
_sym_db.RegisterMessage(TodoCollectionResponse)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class TodosStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.addTodo = channel.unary_unary(
          '/todo.Todos/addTodo',
          request_serializer=AddTodoRequest.SerializeToString,
          response_deserializer=TodoResponse.FromString,
          )
      self.getTodo = channel.unary_unary(
          '/todo.Todos/getTodo',
          request_serializer=GetTodoRequest.SerializeToString,
          response_deserializer=TodoResponse.FromString,
          )
      self.completeTodo = channel.unary_unary(
          '/todo.Todos/completeTodo',
          request_serializer=CompleteTodoRequest.SerializeToString,
          response_deserializer=TodoResponse.FromString,
          )
      self.getTodosByStatus = channel.unary_unary(
          '/todo.Todos/getTodosByStatus',
          request_serializer=GetByStatusRequest.SerializeToString,
          response_deserializer=TodoCollectionResponse.FromString,
          )
      self.updateStatus = channel.unary_unary(
          '/todo.Todos/updateStatus',
          request_serializer=UpdateStatusRequest.SerializeToString,
          response_deserializer=TodoResponse.FromString,
          )
      self.editTodo = channel.unary_unary(
          '/todo.Todos/editTodo',
          request_serializer=EditTodoRequest.SerializeToString,
          response_deserializer=TodoResponse.FromString,
          )


  class TodosServicer(object):

    def addTodo(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def getTodo(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def completeTodo(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def getTodosByStatus(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def updateStatus(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def editTodo(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_TodosServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'addTodo': grpc.unary_unary_rpc_method_handler(
            servicer.addTodo,
            request_deserializer=AddTodoRequest.FromString,
            response_serializer=TodoResponse.SerializeToString,
        ),
        'getTodo': grpc.unary_unary_rpc_method_handler(
            servicer.getTodo,
            request_deserializer=GetTodoRequest.FromString,
            response_serializer=TodoResponse.SerializeToString,
        ),
        'completeTodo': grpc.unary_unary_rpc_method_handler(
            servicer.completeTodo,
            request_deserializer=CompleteTodoRequest.FromString,
            response_serializer=TodoResponse.SerializeToString,
        ),
        'getTodosByStatus': grpc.unary_unary_rpc_method_handler(
            servicer.getTodosByStatus,
            request_deserializer=GetByStatusRequest.FromString,
            response_serializer=TodoCollectionResponse.SerializeToString,
        ),
        'updateStatus': grpc.unary_unary_rpc_method_handler(
            servicer.updateStatus,
            request_deserializer=UpdateStatusRequest.FromString,
            response_serializer=TodoResponse.SerializeToString,
        ),
        'editTodo': grpc.unary_unary_rpc_method_handler(
            servicer.editTodo,
            request_deserializer=EditTodoRequest.FromString,
            response_serializer=TodoResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'todo.Todos', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaTodosServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def addTodo(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def getTodo(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def completeTodo(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def getTodosByStatus(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def updateStatus(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def editTodo(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaTodosStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def addTodo(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    addTodo.future = None
    def getTodo(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    getTodo.future = None
    def completeTodo(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    completeTodo.future = None
    def getTodosByStatus(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    getTodosByStatus.future = None
    def updateStatus(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    updateStatus.future = None
    def editTodo(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    editTodo.future = None


  def beta_create_Todos_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('todo.Todos', 'addTodo'): AddTodoRequest.FromString,
      ('todo.Todos', 'completeTodo'): CompleteTodoRequest.FromString,
      ('todo.Todos', 'editTodo'): EditTodoRequest.FromString,
      ('todo.Todos', 'getTodo'): GetTodoRequest.FromString,
      ('todo.Todos', 'getTodosByStatus'): GetByStatusRequest.FromString,
      ('todo.Todos', 'updateStatus'): UpdateStatusRequest.FromString,
    }
    response_serializers = {
      ('todo.Todos', 'addTodo'): TodoResponse.SerializeToString,
      ('todo.Todos', 'completeTodo'): TodoResponse.SerializeToString,
      ('todo.Todos', 'editTodo'): TodoResponse.SerializeToString,
      ('todo.Todos', 'getTodo'): TodoResponse.SerializeToString,
      ('todo.Todos', 'getTodosByStatus'): TodoCollectionResponse.SerializeToString,
      ('todo.Todos', 'updateStatus'): TodoResponse.SerializeToString,
    }
    method_implementations = {
      ('todo.Todos', 'addTodo'): face_utilities.unary_unary_inline(servicer.addTodo),
      ('todo.Todos', 'completeTodo'): face_utilities.unary_unary_inline(servicer.completeTodo),
      ('todo.Todos', 'editTodo'): face_utilities.unary_unary_inline(servicer.editTodo),
      ('todo.Todos', 'getTodo'): face_utilities.unary_unary_inline(servicer.getTodo),
      ('todo.Todos', 'getTodosByStatus'): face_utilities.unary_unary_inline(servicer.getTodosByStatus),
      ('todo.Todos', 'updateStatus'): face_utilities.unary_unary_inline(servicer.updateStatus),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Todos_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('todo.Todos', 'addTodo'): AddTodoRequest.SerializeToString,
      ('todo.Todos', 'completeTodo'): CompleteTodoRequest.SerializeToString,
      ('todo.Todos', 'editTodo'): EditTodoRequest.SerializeToString,
      ('todo.Todos', 'getTodo'): GetTodoRequest.SerializeToString,
      ('todo.Todos', 'getTodosByStatus'): GetByStatusRequest.SerializeToString,
      ('todo.Todos', 'updateStatus'): UpdateStatusRequest.SerializeToString,
    }
    response_deserializers = {
      ('todo.Todos', 'addTodo'): TodoResponse.FromString,
      ('todo.Todos', 'completeTodo'): TodoResponse.FromString,
      ('todo.Todos', 'editTodo'): TodoResponse.FromString,
      ('todo.Todos', 'getTodo'): TodoResponse.FromString,
      ('todo.Todos', 'getTodosByStatus'): TodoCollectionResponse.FromString,
      ('todo.Todos', 'updateStatus'): TodoResponse.FromString,
    }
    cardinalities = {
      'addTodo': cardinality.Cardinality.UNARY_UNARY,
      'completeTodo': cardinality.Cardinality.UNARY_UNARY,
      'editTodo': cardinality.Cardinality.UNARY_UNARY,
      'getTodo': cardinality.Cardinality.UNARY_UNARY,
      'getTodosByStatus': cardinality.Cardinality.UNARY_UNARY,
      'updateStatus': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'todo.Todos', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
