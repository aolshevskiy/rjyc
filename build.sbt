organization := "org.python"

name := "rjyc"

version := "1.0-SNAPSHOT"

resolvers := Seq("SakaiProject Repository" at "http://source.sakaiproject.org/maven2/")

pomIncludeRepository ~= { (filter) => { (repo) =>
	(!repo.root.startsWith("http://scala")) && filter(repo)
} }

libraryDependencies += "org.python" % "jython-complete" % "2.5.1"

unmanagedResourceDirectories in Compile <<= (unmanagedResourceDirectories in Compile, sourceDirectory in Runtime) { (rds, sd) => rds :+ sd / "python" }

crossPaths := false

autoScalaLibrary := false

publishMavenStyle := true

publishTo := Some(Resolver.file("Local", Path.userHome / "projects" / "siasia.github.com" / "maven2" asFile)(Patterns(true, Resolver.mavenStyleBasePattern)))
