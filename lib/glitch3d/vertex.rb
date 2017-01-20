class Vertex
  attr_accessor :x, :y, :z

  def initialize
    @x = x
    @y = y
    @z = z
  end

  def to_s
    "v #{x} #{y} #{z}"
  end

  def alter(vertex)
    v = vertex.dup
    v.send("#{[:x, :y, :z].sample}+=", rand_vertex_glitch_offset)
    v
  end

  def self.furthest(vertices_list)
    furthest_vertices = [
      vertices_list.max_by { |v| v.x },
      vertices_list.max_by { |v| v.y },
      vertices_list.max_by { |v| v.z }
    ]
    max_coord = [
      furthest_vertices[0].x,
      furthest_vertices[1].y,
      furthest_vertices[2].z
    ].max
    furthest_vertices.find { |v| v.x == max_coord || v.y == max_coord || v.z == max_coord }
  end
end